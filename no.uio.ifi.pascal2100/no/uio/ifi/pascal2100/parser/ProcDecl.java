package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;

import no.uio.ifi.pascal2100.main.*;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>ProcDecl</h1>
 *
 * <p>Parse a Pascal ProcDecl as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class ProcDecl extends PascalDecl {
Block b;
ParamDeclList pdl;
public  String name ;
public ProcDecl nextproc;
public ArrayList <ProcDecl> procdecllist = new ArrayList<ProcDecl>();

	public ProcDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}

	

    /**
     * Parse a ProcDecl.
     * @param Scanner Tokens.
     * @return the ProcDecl object of the parse tree.
     * procedure ---name--- param decl list--- ; -----block----- ;---
     */
	public static ProcDecl parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("proc decl");
		ProcDecl pd= new ProcDecl(s.curToken.id,s.curLineNum());
		s.skip(procedureToken);
		s.test(nameToken);
		pd.name=s.curToken.id;
		pd.procdecllist.add(pd);
		s.readNextToken();
		if( s.curToken.kind ==  leftParToken)
		 {
			pd.pdl=ParamDeclList.parse(s);pd.pdl.procDecl=pd;
		 
		 }
		
		s.skip(semicolonToken);
		
		pd.b=Block.parse(s);pd.b.prcDc=pd;
		
		s.skip(semicolonToken);
		leaveParser("proc decl");
		
		return pd;
	}
	
		@Override public String identify() {
			return "<proc decl> " +name+ " on line " + lineNum;
			
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		
		Main.log.prettyPrint("procedure");Main.log.prettyPrint(name);
		if (pdl!=null)pdl.prettyPrint();Main.log.prettyPrint(";");
		b.prettyPrint();Main.log.prettyPrint(";");
		
	}



	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		
		if(pdl != null){
			pdl.check(curScope, lib);
			for (ParamDecl pd: pdl.paramdecls) {
				curScope.addDecl(pd.name, pd);
				System.out.println("proc name"+pd.name);
				
				} 
		}
		if(b!=null) {
			b.outerScope= b;
			b.check(curScope, lib);
		}
		
		
	}
}
