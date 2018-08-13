package no.uio.ifi.pascal2100.parser;


import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>ParamDeclList</h1>
 *
 * <p>Parse a Pascal ParamDeclList as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */

public class ParamDeclList extends PascalSyntax {

	public FuncDecl fndecl;
	public ProcDecl procDecl;
	public static List <ParamDecl>paramdecllist = new ArrayList<ParamDecl>(); 
	
	ParamDecl pd;
	ParamDecl firstpd;
	public ArrayList <ParamDecl>paramdecls = new ArrayList<ParamDecl>();
	 
	

	public ParamDeclList(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<param decl list> " + " on line " + lineNum;
	}
	
	

    /**
     * Parse a ParamDeclList.
     * @param Scanner Tokens.
     * @return the Block ParamDeclList of the parse tree.
     * ---( ---param decl-----;----)----
     */
	public static ParamDeclList parse(Scanner s) {
		enterParser("param decl list");
		s.skip(leftParToken);
		
		ParamDeclList pdl = new ParamDeclList( s.curLineNum());
		pdl.firstpd = ParamDecl.parse(s);
		pdl.paramdecls.add(pdl.firstpd);
		ParamDecl tempPd=pdl.firstpd;
		
		
			while (s.curToken.kind == semicolonToken){
				s.skip(semicolonToken);
			tempPd.nextpd= tempPd=ParamDecl. parse(s);
			pdl.paramdecls.add(tempPd);	
		}
		
		s.skip(rightParToken);
	
		leaveParser("param decl list");
		
		return pdl;
		}


	@Override void prettyPrint() {
	Main.log.prettyPrint("( "); 
	
	ParamDecl localpd= firstpd;
	while (localpd!=null){
		localpd.prettyPrint();
	
	localpd=localpd.nextpd;
	if(localpd != null)Main.log.prettyPrint(" ; ");
	
	}
	 Main.log.prettyPrint(" )");
	 Main.log.prettyIndent();
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		ParamDecl localpd= firstpd;
		while (localpd!=null){
			localpd.check(curScope, lib);
		
		localpd=localpd.nextpd;
		
		
		}
		
	}

}