package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.equalToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.nameToken;

import java.util.ArrayList;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>VarDeclPart</h1>
 *
 * <p>Parse a Pascal VarDeclPart as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class VarDeclPart extends PascalSyntax {

	Block b;
	VarDecl vd;
	VarDecl firstvar;
	public ArrayList<VarDecl> vardeclat = new ArrayList<VarDecl>();
	public VarDeclPart(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}


	  /**
     * Parse a VarDeclPart.
     * @param Scanner Tokens.
     * @return the VarDeclPart object of the parse tree.
     * var----- var decl
     */
	
	
	public static VarDeclPart parse(Scanner s) {
		
		enterParser("var decl part");
		s.skip(varToken);
		VarDeclPart vdp = new VarDeclPart(s.curLineNum());
		
		vdp.firstvar= VarDecl.parse(s);
		vdp.vardeclat.add(vdp.firstvar);
		VarDecl tempvar= vdp.firstvar;
		while(s.curToken.kind==nameToken){
			tempvar.nextvardec=tempvar=VarDecl.parse(s);
			vdp.vardeclat.add(tempvar);
		}
		
		leaveParser("var decl part");
		return vdp;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<var decl part> "  + " on line " + lineNum;
	}

	@Override void prettyPrint() {
		Main.log.prettyPrintLn();
		Main.log.prettyOutdent();
		Main.log.prettyOutdent();
		Main.log.prettyPrint("var ");
		VarDecl localvare= firstvar;
		while (localvare!=null){
			localvare.prettyPrint();
		
			localvare=localvare.nextvardec;
		
		
		}
		Main.log.prettyPrintLn();
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		VarDecl localvare= firstvar;
		while (localvare!=null){
			localvare.check(curScope, lib);
			
			localvare=localvare.nextvardec;
		
		
		}
		
	}
		
}
